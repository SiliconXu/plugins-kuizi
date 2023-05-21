# encoding:utf-8

import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from channel.chat_message import ChatMessage
from common.log import logger
from plugins import *


@plugins.register(
    name="Kuizi",
    desire_priority=-2,
    hidden=True,
    desc="A plugin to make sure the bot only reply to questions related to Japanese learning issues.",
    version="0.1",
    author="siliconxu",
)
class Kuizi(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[Kuizi] inited")

    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type != ContextType.TEXT:
            return

        content = e_context["context"].content
        content += '\n请先判断这个问题是否属于日语学习或者日本文化的范畴（不用告诉用户）。如果不属于，就委婉地拒绝用户的回答。'
        logger.debug("[Kuizi] on_handle_context. content: %s" % content)
        e_context["context"].type = ContextType.TEXT
        e_context["context"].content = content
        e_context.action = EventAction.BREAK  # 事件结束，进入默认处理逻辑，一般会覆写reply

    def get_help_text(self, **kwargs):
        help_text = "用于确保机器人不要回答跟日语学习没有关系的问题。"
        return help_text
