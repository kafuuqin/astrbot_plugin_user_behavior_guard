from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star

from .behavior_guard import check_behavior


class UserBehaviorGuardPlugin(Star):
    """Expose the behavior-checking test stub as an AstrBot LLM tool."""

    def __init__(self, context: Context):
        super().__init__(context)

    @filter.llm_tool(name="check_user_behavior")
    async def check_user_behavior(self, event: AstrMessageEvent, behavior: str) -> str:
        """Check a proposed behavior against the behavior constraints.

        This test version always returns YES. It only tests tool invocation
        and does not perform a real compliance assessment. YES cannot override
        other constraints. The result contract is YES = allowed, NO = disallowed.

        Args:
            behavior(string): Proposed behavior or reply and the context needed to assess it.

        Returns:
            The literal string YES in this test version.
        """
        return check_behavior(behavior)
