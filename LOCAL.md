## 📦 安装

**从源码安装**（最新功能，推荐用于开发）

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e .
```

## 🚀 快速开始

> [!TIP]
> 在 `~/.nanobot/config.json` 中设置 API key。
> 获取 API key：[OpenRouter](https://openrouter.ai/keys)（全球）· [DashScope](https://dashscope.console.aliyun.com)（通义千问）· [Brave Search](https://brave.com/search/api/)（可选，用于网络搜索）

**1. 初始化**

```bash
nanobot onboard
```

**2. 配置** (`~/.nanobot/config.json`)

对于 OpenRouter — 推荐全球用户使用：

```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4-5"
    }
  }
}
```

**3. 开始对话**

```bash
nanobot agent -m "2+2 等于多少？"
```

只需 2 分钟，你就能拥有一个可用的 AI 助手！

## 🖥️ 本地模型（vLLM）

使用 vLLM 或任何 OpenAI 兼容服务器，让 nanobot 运行你自己的本地模型。

**1. 启动 vLLM 服务器**

```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000
```

**2. 配置** (`~/.nanobot/config.json`)

```json
{
  "providers": {
    "vllm": {
      "apiKey": "dummy",
      "apiBase": "http://localhost:8000/v1"
    }
  },
  "agents": {
    "defaults": {
      "model": "meta-llama/Llama-3.1-8B-Instruct"
    }
  }
}
```

**3. 开始对话**

```bash
nanobot agent -m "你好，来自本地 LLM！"
```

> [!TIP]
> 对于不需要身份验证的本地服务器，`apiKey` 可以是任意非空字符串。

## 💬 聊天应用

通过 Telegram、Discord、WhatsApp、飞书、钉钉、Slack、Email 或 QQ 与你的 nanobot 对话 — 随时随地。

| 频道         | 难度                        |
| ------------ | --------------------------- |
| **Telegram** | 简单（只需 token）          |
| **Discord**  | 简单（bot token + intents） |
| **WhatsApp** | 中等（扫码）                |
| **Feishu**   | 中等（应用凭证）            |
| **DingTalk** | 中等（应用凭证）            |
| **Slack**    | 中等（bot + app token）     |
| **Email**    | 中等（IMAP/SMTP 凭证）      |
| **QQ**       | 简单（应用凭证）            |

<details>
<summary><b>Telegram</b>（推荐）</summary>

**1. 创建机器人**

- 打开 Telegram，搜索 `@BotFather`
- 发送 `/newbot`，按提示操作
- 复制 token

**2. 配置**

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "allowFrom": ["YOUR_USER_ID"]
    }
  }
}
```

> 你可以在 Telegram 设置中找到你的**用户 ID**，显示为 `@yourUserId`。
> 复制这个值时**去掉 `@ 符号**并粘贴到配置文件中。

**3. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Discord</b></summary>

**1. 创建机器人**

- 访问 https://discord.com/developers/applications
- 创建应用 → Bot → 添加 Bot
- 复制 bot token

**2. 启用 intents**

- 在 Bot 设置中，启用 **MESSAGE CONTENT INTENT**
- （可选）如果你计划基于成员数据使用白名单，启用 **SERVER MEMBERS INTENT**

**3. 获取你的用户 ID**

- Discord 设置 → 高级 → 启用 **开发者模式**
- 右键点击你的头像 → **复制用户 ID**

**4. 配置**

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "allowFrom": ["YOUR_USER_ID"]
    }
  }
}
```

**5. 邀请机器人**

- OAuth2 → URL Generator
- Scopes: `bot`
- Bot Permissions: `Send Messages`, `Read Message History`
- 打开生成的邀请 URL 并将机器人添加到你的服务器

**6. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>WhatsApp</b></summary>

需要 **Node.js ≥18**。

**1. 关联设备**

```bash
nanobot channels login
# 用 WhatsApp 扫码 → 设置 → 关联设备
```

**2. 配置**

```json
{
  "channels": {
    "whatsapp": {
      "enabled": true,
      "allowFrom": ["+1234567890"]
    }
  }
}
```

**3. 运行**（两个终端）

```bash
# 终端 1
nanobot channels login

# 终端 2
nanobot gateway
```

</details>

<details>
<summary><b>飞书 (Feishu)</b></summary>

使用 **WebSocket** 长连接 — 不需要公网 IP。

**1. 创建飞书机器人**

- 访问 [飞书开放平台](https://open.feishu.cn/app)
- 创建新应用 → 启用 **Bot** 能力
- **权限**：添加 `im:message`（发送消息）
- **事件**：添加 `im.message.receive_v1`（接收消息）
  - 选择 **长连接** 模式（需要先运行 nanobot 来建立连接）
- 从"凭证与基础信息"获取 **App ID** 和 **App Secret**
- 发布应用

**2. 配置**

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_xxx",
      "appSecret": "xxx",
      "encryptKey": "",
      "verificationToken": "",
      "allowFrom": []
    }
  }
}
```

> `encryptKey` 和 `verificationToken` 在长连接模式下是可选的。
> `allowFrom`：留空允许所有用户，或添加 `["ou_xxx"]` 限制访问。

**3. 运行**

```bash
nanobot gateway
```

> [!TIP]
> 飞书使用 WebSocket 接收消息 — 不需要 webhook 或公网 IP！

</details>

<details>
<summary><b>QQ 单聊</b></summary>

使用 **botpy SDK** 配合 WebSocket — 不需要公网 IP。目前仅支持**私聊**。

**1. 注册并创建机器人**

- 访问 [QQ 开放平台](https://q.qq.com) → 注册成为开发者（个人或企业）
- 创建新的机器人应用
- 进入 **开发设置** → 复制 **AppID** 和 **AppSecret**

**2. 设置沙箱进行测试**

- 在机器人管理控制台，找到 **沙箱配置**
- 在 **消息列表配置** 下，点击 **添加成员** 并添加你自己的 QQ 号
- 添加成功后，用手机 QQ 扫描机器人二维码 → 打开机器人资料 → 点击"发消息"开始聊天

**3. 配置**

> - `allowFrom`：留空允许所有人访问，或添加用户 openid 限制访问。你可以在 nanobot 日志中找到用户发送消息时的 openid。
> - 生产环境：在机器人控制台提交审核并发布。查看 [QQ 机器人文档](https://bot.q.qq.com/wiki/) 获取完整的发布流程。

```json
{
  "channels": {
    "qq": {
      "enabled": true,
      "appId": "YOUR_APP_ID",
      "secret": "YOUR_APP_SECRET",
      "allowFrom": []
    }
  }
}
```

**4. 运行**

```bash
nanobot gateway
```

现在给机器人发送消息 — 它应该会回复你！

</details>

<details>
<summary><b>钉钉 (DingTalk)</b></summary>

使用 **流模式** — 不需要公网 URL。

**1. 创建钉钉机器人**

- 访问 [钉钉开放平台](https://open-dev.dingtalk.com/)
- 创建新应用 → 添加 **机器人** 能力
- **配置**：
  - 开启 **流模式**
- **权限**：添加发送消息所需的权限
- 从"凭证"获取 **AppKey**（Client ID）和 **AppSecret**（Client Secret）
- 发布应用

**2. 配置**

```json
{
  "channels": {
    "dingtalk": {
      "enabled": true,
      "clientId": "YOUR_APP_KEY",
      "clientSecret": "YOUR_APP_SECRET",
      "allowFrom": []
    }
  }
}
```

> `allowFrom`：留空允许所有用户，或添加 `["staffId"]` 限制访问。

**3. 运行**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Slack</b></summary>

使用 **Socket 模式** — 不需要公网 URL。

**1. 创建 Slack 应用**

- 访问 [Slack API](https://api.slack.com/apps) → **创建新应用** → "从零开始"
- 选择名称并选择你的工作区

**2. 配置应用**

- **Socket 模式**：开启 → 生成具有 `connections:write` 范围的 **应用级 token** → 复制它（`xapp-...`）
- **OAuth & Permissions**：添加 bot 作用域：`chat:write`, `reactions:write`, `app_mentions:read`
- **事件订阅**：开启 → 订阅 bot 事件：`message.im`, `message.channels`, `app_mention` → 保存更改
- **应用首页**：滚动到 **显示标签** → 启用 **消息标签** → 勾选 **"允许用户从消息标签发送斜杠命令和消息"**
- **安装应用**：点击 **安装到工作区** → 授权 → 复制 **Bot Token**（`xoxb-...`）

**3. 配置 nanobot**

```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "botToken": "xoxb-...",
      "appToken": "xapp-...",
      "groupPolicy": "mention"
    }
  }
}
```

**4. 运行**

```bash
nanobot gateway
```

直接私信机器人或在频道中 @mention 它 — 它应该会回复你！

> [!TIP]
>
> - `groupPolicy`：`"mention"`（默认 — 仅在 @mention 时回复），`"open"`（回复所有频道消息），或 `"allowlist"`（限制为特定频道）。
> - DM 策略默认为开放。设置 `"dm": {"enabled": false}` 禁用 DM。

</details>

<details>
<summary><b>Email</b></summary>

给 nanobot 一个专用的邮箱账户。它通过 **IMAP** 轮询接收邮件，并通过 **SMTP** 回复 — 就像一个个人邮件助手。

**1. 获取凭证（Gmail 示例）**

- 为你的机器人创建一个专用的 Gmail 账户（如 `my-nanobot@gmail.com`）
- 启用两步验证 → 创建[应用密码](https://myaccount.google.com/apppasswords)
- 将此应用密码用于 IMAP 和 SMTP

**2. 配置**

> - `consentGranted` 必须为 `true` 才能允许邮箱访问。这是一个安全门 — 设置为 `false` 完全禁用。
> - `allowFrom`：留空接受来自任何人的邮件，或限制特定发件人。
> - `smtpUseTls` 和 `smtpUseSsl` 默认分别为 `true` / `false`，这对于 Gmail（端口 587 + STARTTLS）是正确的。不需要显式设置。
> - 如果你只想阅读/分析邮件而不自动回复，设置 `"autoReplyEnabled": false`。

```json
{
  "channels": {
    "email": {
      "enabled": true,
      "consentGranted": true,
      "imapHost": "imap.gmail.com",
      "imapPort": 993,
      "imapUsername": "my-nanobot@gmail.com",
      "imapPassword": "your-app-password",
      "smtpHost": "smtp.gmail.com",
      "smtpPort": 587,
      "smtpUsername": "my-nanobot@gmail.com",
      "smtpPassword": "your-app-password",
      "fromAddress": "my-nanobot@gmail.com",
      "allowFrom": ["your-real-email@gmail.com"]
    }
  }
}
```

**3. 运行**

```bash
nanobot gateway
```

</details>

## ⚙️ 配置

配置文件：`~/.nanobot/config.json`

### Provider

> [!TIP]
>
> - **Groq** 通过 Whisper 提供免费的语音转文字。如果配置了，Telegram 语音消息将自动转录。
> - **智谱编程计划**：如果你使用的是智谱编程计划，在 zhipu provider 配置中设置 `"apiBase": "https://open.bigmodel.cn/api/coding/paas/v4"`。

| Provider     | 用途                                | 获取 API Key                                                         |
| ------------ | ----------------------------------- | -------------------------------------------------------------------- |
| `openrouter` | LLM（推荐，访问所有模型）           | [openrouter.ai](https://openrouter.ai)                               |
| `anthropic`  | LLM（Claude 直连）                  | [console.anthropic.com](https://console.anthropic.com)               |
| `openai`     | LLM（GPT 直连）                     | [platform.openai.com](https://platform.openai.com)                   |
| `deepseek`   | LLM（DeepSeek 直连）                | [platform.deepseek.com](https://platform.deepseek.com)               |
| `groq`       | LLM + **语音转文字**（Whisper）     | [console.groq.com](https://console.groq.com)                         |
| `gemini`     | LLM（Gemini 直连）                  | [aistudio.google.com](https://aistudio.google.com)                   |
| `aihubmix`   | LLM（API 网关，访问所有模型）       | [aihubmix.com](https://aihubmix.com)                                 |
| `dashscope`  | LLM（通义千问）                     | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) |
| `moonshot`   | LLM（月之暗面/Kimi）                | [platform.moonshot.cn](https://platform.moonshot.cn)                 |
| `zhipu`      | LLM（智谱 GLM）                     | [open.bigmodel.cn](https://open.bigmodel.cn)                         |
| `vllm`       | LLM（本地，任何 OpenAI 兼容服务器） | —                                                                    |

<details>
<summary><b>新增 Provider（开发者指南）</b></summary>

nanobot 使用 **Provider Registry**（`nanobot/providers/registry.py`）作为唯一的事实来源。
新增 provider 只需 **2 步** — 无需修改 if-elif 链。

**第 1 步。** 在 `nanobot/providers/registry.py` 的 `PROVIDERS` 中添加 `ProviderSpec` 条目：

```python
ProviderSpec(
    name="myprovider",                   # 配置字段名
    keywords=("myprovider", "mymodel"),  # 用于自动匹配的模型名称关键词
    env_key="MYPROVIDER_API_KEY",       # LiteLLM 的环境变量
    display_name="My Provider",          # 在 `nanobot status` 中显示
    litellm_prefix="myprovider",         # 自动前缀：model → myprovider/model
    skip_prefixes=("myprovider/",),      # 不要双重前缀
)
```

**第 2 步。** 在 `nanobot/config/schema.py` 的 `ProvidersConfig` 中添加字段：

```python
class ProvidersConfig(BaseModel):
    ...
    myprovider: ProviderConfig = ProviderConfig()
```

就这样！环境变量、模型前缀、配置匹配和 `nanobot status` 显示都会自动工作。

**常用 `ProviderSpec` 选项：**

| 字段                     | 描述                              | 示例                                     |
| ------------------------ | --------------------------------- | ---------------------------------------- |
| `litellm_prefix`         | 自动为模型名添加前缀              | `"dashscope"` → `dashscope/qwen-max`     |
| `skip_prefixes`          | 如果模型已以这些开头则不添加前缀  | `("dashscope/", "openrouter/")`          |
| `env_extras`             | 要设置的其他环境变量              | `(("ZHIPUAI_API_KEY", "{api_key}"),)`    |
| `model_overrides`        | 每个模型的参数覆盖                | `(("kimi-k2.5", {"temperature": 1.0}),)` |
| `is_gateway`             | 可以路由任何模型（如 OpenRouter） | `True`                                   |
| `detect_by_key_prefix`   | 通过 API key 前缀检测网关         | `"sk-or-"`                               |
| `detect_by_base_keyword` | 通过 API base URL 关键词检测网关  | `"openrouter"`                           |
| `strip_model_prefix`     | 在重新添加前缀前剥离现有前缀      | `True`（用于 AiHubMix）                  |

</details>

### 安全

> 对于生产部署，在配置中设置 `"restrictToWorkspace": true` 来沙箱化代理。

| 选项                        | 默认值           | 描述                                                                                                  |
| --------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------- |
| `tools.restrictToWorkspace` | `false`          | 当为 `true` 时，限制**所有**代理工具（shell、文件读写编辑、列表）到工作目录。防止路径遍历和越权访问。 |
| `channels.*.allowFrom`      | `[]`（允许所有） | 用户 ID 白名单。空 = 允许所有人；非空 = 仅列出的用户可以交互。                                        |

## CLI 参考

| 命令                          | 描述                  |
| ----------------------------- | --------------------- |
| `nanobot onboard`             | 初始化配置和工作区    |
| `nanobot agent -m "..."`      | 与代理对话            |
| `nanobot agent`               | 交互式对话模式        |
| `nanobot agent --no-markdown` | 显示纯文本回复        |
| `nanobot agent --logs`        | 对话时显示运行时日志  |
| `nanobot gateway`             | 启动网关              |
| `nanobot status`              | 显示状态              |
| `nanobot channels login`      | 关联 WhatsApp（扫码） |
| `nanobot channels status`     | 显示频道状态          |

交互模式退出：`exit`、`quit`、`/exit`、`/quit`、`:q` 或 `Ctrl+D`。

<details>
<summary><b>定时任务（Cron）</b></summary>

```bash
# 添加任务
nanobot cron add --name "daily" --message "早上好！" --cron "0 9 * * *"
nanobot cron add --name "hourly" --message "检查状态" --every 3600

# 列出任务
nanobot cron list

# 移除任务
nanobot cron remove <job_id>
```

</details>

## 📁 项目结构

```
nanobot/
├── agent/          # 🧠 核心代理逻辑
│   ├── loop.py     #    代理循环（LLM ↔ 工具执行）
│   ├── context.py  #    提示词构建器
│   ├── memory.py   #    持久化内存
│   ├── skills.py   #    技能加载器
│   ├── subagent.py #    后台任务执行
│   └── tools/      #    内置工具（包括 spawn）
├── skills/         # 🎯 捆绑技能（github、weather、tmux...）
├── channels/       # 📱 WhatsApp 集成
├── bus/            # 🚌 消息路由
├── cron/           # ⏰ 定时任务
├── heartbeat/      # 💓 主动唤醒
├── providers/      # 🤖 LLM provider（OpenRouter 等）
├── session/        # 💬 对话会话
├── config/         # ⚙️ 配置
└── cli/            # 🖥️ 命令行
```
