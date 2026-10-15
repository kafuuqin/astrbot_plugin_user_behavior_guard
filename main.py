from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star

from .behavior_guard import check_behavior


class UserBehaviorGuardPlugin(Star):
    """Expose user behavior compliance analysis as an AstrBot LLM tool."""

    def __init__(self, context: Context):
        super().__init__(context)

    @filter.llm_tool(name="check_user_behavior")
    async def check_user_behavior(self, event: AstrMessageEvent, behavior: str) -> str:
        """分析用户行为是否合规，根据行为描述和相关上下文返回判断结果。

        当需要判断用户的言论、请求或行为是否符合行为约束时调用。
        返回 YES 表示合规，NO 表示不合规。

        Args:
            behavior(string): 需要分析的用户言论、请求或行为，以及判断所需的相关上下文。

        Returns:
            YES 表示合规，NO 表示不合规。
        """
        return check_behavior(behavior)
