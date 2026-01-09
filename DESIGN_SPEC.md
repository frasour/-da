# 博客平台 设计规格说明

版本：1.0
编制：项目组
日期：2025-12-06

## 1 项目简介

### 1.1 目标与范围
本设计规格说明（Design Specification）基于项目《博客平台——愿景与范围》与《博客平台需求规格说明》，对系统的设计层面进行详细描述，包括体系架构、模块划分、接口定义、数据模型、部署方案及关键质量属性（性能、安全、可维护性）。

首发范围（版本1）：
- 前台：文章浏览/分页/搜索、文章详情（Markdown 渲染）、时间轴、标签/分类、相册展示、友链、音乐播放等；
- 用户：注册/登录、个人资料、头像、评论/留言；
- 管理端：文章/分类/标签/相册/友链/评论管理；
- 服务端：RESTful API（JWT 鉴权）、MySQL 数据持久化、对象存储支持（本地/MinIO/云存储）。

不包含实时协同编辑、广告竞价或原生移动端应用（见范围限制）。

### 1.2 术语和缩写
- JWT: JSON Web Token
- API: 应用程序编程接口
- CDN: 内容分发网络
- MinIO: 对象存储服务

### 1.3 引用文档
- `作业1-博客平台愿景与范围.docx`
- `作业2-博客平台需求规格说明.docx`
- 项目代码仓库：`blog/`, `blog-admin/`, `blog-server/`

## 2 总体描述

### 2.1 产品前景与功能
系统为前后端分离的响应式 Web 博客平台，覆盖桌面与移动端浏览器，面向读者、注册用户与作者/管理员。主要功能点：
- 文章列表、详情、搜索、相关推荐、SEO 友好路由；
- 编辑器支持 Markdown（富文本预览）、图片/相册管理、草稿与定时发布（后续版本）；
- 评论、点赞、通知（站内消息）；
- 后台管理：内容 CRUD、评论审核、用户与权限管理；
- 提供稳定的 RESTful API，支持前台与管理端调用。

### 2.2 设计约束
- 前端技术栈：Vue 3、Vite、Element Plus、Pinia、Axios、TailwindCSS；
- 后端技术栈：Node.js (Koa)、Sequelize、MySQL；
- 部署：支持 HTTPS、反向代理、静态资源缓存；对象存储用于媒体资源。

### 2.3 假设与依赖
- 存在可用的 MySQL 实例与对象存储服务；
- 用户使用现代浏览器并启用 JavaScript；
- 第三方库在支持版本内稳定。

## 3 软件架构设计

### 3.1 接口设计

#### 3.1.1 用户接口（前端视角）
- 主页/文章列表: GET /api/articles?page={}&size={}&tag={}&category={}
- 文章详情: GET /api/articles/{id}
- 用户注册: POST /api/auth/register
- 用户登录: POST /api/auth/login -> 返回 JWT
- 发表评论: POST /api/articles/{id}/comments (需 Authorization)
- 管理端登录/内容管理: /api/admin/** 系列接口（需基于角色的权限）

（注：以上接口为高层约定；具体字段、返回码在后端接口文档中定义）

#### 3.1.2 软件/通讯接口
- REST API 使用 JSON 格式通信，鉴权采用 Authorization: Bearer <token>；
- 静态资源与媒体通过对象存储或 CDN 分发，上传接口返回媒体 URL；
- 支持跨域（CORS）配置以允许前后端分离部署。

### 3.2 软件架构模型设计

系统采用前后端分离、单体后端服务（可在未来拆分微服务）的分层架构：
- 前端（blog/ 与 blog-admin/）：UI 层、状态管理（Pinia）、路由与网络层（Axios）；
- 后端（blog-server/）：路由层（koa-router）、控制器层、服务层、数据访问层（Sequelize）；
- 数据存储：MySQL（关系数据）、对象存储（图片/媒体）；
- 辅助：反向代理（Nginx）、可选 CDN、日志与监控组件。

模块划分（核心模块）
- auth：认证与授权（JWT、密码哈希、角色权限）；
- article：文章相关（CRUD、草稿、发布、Markdown 渲染）；
- comment：评论与审核；
- media：图片/相册上传与管理；
- tag/category：标签/分类管理；
- user：用户资料与设置；
- admin：后台管理相关接口与操作日志；
- notify：站内通知与消息队列（轻量实现）。

## 4 用例设计（示例）

### UC-01: 浏览文章列表
- 参与者：访客/注册用户
- 前置条件：服务可用
- 主成功场景：用户访问 /，后端返回分页文章列表，前端渲染卡片与分页组件。
- 非功能需求：列表页 p95 响应时间 ≤ 2s；支持按标签/分类筛选。

### UC-02: 查看文章详情
- 参与者：所有用户
- 主成功场景：访问文章详情页，渲染 Markdown 内容、评论区、相关推荐。
- 特殊需求：代码高亮、图片懒加载、XSS 防护。

（其余用例见 `作业2-博客平台需求规格说明`，按模板补全）

## 5 模块详细设计（示例模块）

### 5.1 模块：article-service
- 责任：管理文章的创建、编辑、发布、查询与索引。
- 接口：
  - createArticle(userId, articleData) -> articleId
  - updateArticle(articleId, articleData)
  - publishArticle(articleId)
  - listArticles(queryParams) -> pagedResult
  - getArticleById(articleId) -> articleData (包括关联评论/推荐)
- 数据流：前端 -> API 控制器 -> service 层 -> DAO (Sequelize) -> MySQL
- 错误处理：校验必填字段、权限校验、事务回滚（在需要时）。

### 5.2 模块：comment-service
- 支持内容校验、敏感词过滤、审核队列、分页查询、按文章/时间筛选。

## 6 数据模型设计（概要）

建议的主要关系型表：
- users (id, username, email, password_hash, role, avatar, created_at, updated_at)
- articles (id, author_id, title, slug, content, summary, cover_url, status, published_at, created_at, updated_at)
- categories (id, name, slug, created_at)
- tags (id, name, slug)
- article_tags (article_id, tag_id)
- comments (id, article_id, user_id, parent_id, content, status, created_at)
- photos (id, album_id, url, width, height, created_at)
- links (id, title, url, description, created_at)
- music (id, title, source, url, meta)

索引与性能：对 `articles(published_at)`、`articles(slug)`、`comments(article_id)` 建立索引；对常用检索字段开启全文索引（视数据库支持）。

## 7 部署模型设计

基础部署建议（版本1）：
- 前端：构建为静态文件，通过 Nginx 托管并反向代理到后端 API；
- 后端：Node.js 应用（blog-server）运行在 PM2 或容器内，连接 MySQL 与对象存储；
- 反向代理与 HTTPS：Nginx 配置 TLS、缓存静态资源、代理 /api/* 到后端；
- 缩放：可基于负载均衡器扩展后端实例；对象存储与 CDN 用于静态资源分发。

部署图示（文本）：
- 用户 -> CDN/Nginx -> (静态前端) ; Nginx -> /api -> 后端实例 -> MySQL / 对象存储

## 8 其它设计模型

可选：
- 审计日志表（记录管理员操作）；
- 操作异步化（如图片处理、邮件/通知）通过队列（RabbitMQ/Redis streams）；
- 定期备份（MySQL 备份脚本、对象存储生命周期管理）。

## 9 AI 辅助设计总结

本项目文档中采用 AI 辅助梳理需求与生成用例示例，AI 产出仅作为草案，需由项目成员审阅并融入实际实现细节。建议在迭代时使用 AI 生成的变更摘要与测试用例草案以加速开发节奏。

## 附录
- 参考：`作业1-博客平台愿景与范围.docx`, `作业2-博客平台需求规格说明(1).docx`, 仓库源码

---

（结束）
