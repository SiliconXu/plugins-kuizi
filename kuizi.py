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
        content += '\n请先判断这个问题是否关于日语学习、日语翻译、日语文化的内容。如果不是，就委婉的拒绝用户的回答。'
        logger.debug("[Kuizi] on_handle_context. content: %s" % content)
        # # pattern = re.compile("[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]+")
        # reply = Reply()
        # reply.type = ReplyType.TEXT
        # msg: ChatMessage = e_context["context"]["msg"]
        # print(msg.content)
        # if e_context["context"]["isgroup"]:
        #     reply.content = msg.content + f"Hello, {msg.actual_user_nickname} from {msg.from_user_nickname}"
        # else:
        #     reply.content = f"Hello, {msg.from_user_nickname}"
        # e_context["reply"] = reply
        e_context["context"].type = ContextType.TEXT
        e_context["context"].content = content
        e_context.action = EventAction.BREAK  # 事件结束，进入默认处理逻辑，一般会覆写reply

    def get_help_text(self, **kwargs):
        help_text = "用于确保机器人不要回答跟日语学习没有关系的问题。"
        return help_text