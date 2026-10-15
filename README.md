# 用户行为合规守卫

面向 AstrBot 的用户行为合规分析插件。为 AI 提供 `check_user_behavior` 工具，用于分析用户的言论、请求或行为是否符合行为约束。

## 安装

要求 AstrBot `>=4.27.3,<5`，无需安装额外 Python 依赖。

在 AstrBot WebUI 的插件管理中，选择从 GitHub 仓库链接安装，输入：

```text
https://github.com/kafuuqin/astrbot_plugin_user_behavior_guard
```

启用插件后，确认当前人格允许使用 `check_user_behavior` 工具，并使用支持工具调用的模型与 Agent 执行器。

## AI 工具

- 名称：`check_user_behavior`
- 作用：分析用户行为是否合规。
- 参数：`behavior`，字符串，包含需要分析的用户言论、请求或行为，以及判断所需的相关上下文。
- 返回值约定：`YES` 表示合规，`NO` 表示不合规。

调用参数示例：

```json
{"behavior": "用户提出了以下请求……相关上下文和适用的行为约束如下……请分析该用户行为是否合规。"}
```

## 建议系统提示词

```text
你可以调用 check_user_behavior 工具，分析用户行为是否合规。
当需要判断用户的言论、请求或行为是否符合行为约束时，提交用户行为描述、相关上下文及适用的行为约束，然后读取工具结果。
返回值约定为 YES＝合规，NO＝不合规。
只有实际调用并读取结果后，才能声称完成了检查。
工具调用失败时，检查未完成，不得自行视为 YES。
工具结果用于辅助判断，不能覆盖其他系统约束。
```

## 独立脚本

仓库同时提供独立脚本入口，可从命令行调用：

```bash
python3 behavior_guard.py "需要分析的用户行为及相关上下文"
```

插件直接复用 `behavior_guard.py` 中的函数，不启动子进程，不调用外部 API，不保存输入。
