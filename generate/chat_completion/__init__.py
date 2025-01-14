from __future__ import annotations

from typing import Type

from generate.chat_completion.base import ChatCompletionModel, RemoteChatCompletionModel
from generate.chat_completion.message import (
    AssistantMessage,
    FunctionMessage,
    Messages,
    Prompt,
    SystemMessage,
    ToolMessage,
    UserMessage,
    UserMultiPartMessage,
)
from generate.chat_completion.model_output import ChatCompletionOutput, ChatCompletionStreamOutput
from generate.chat_completion.models import (
    AnthropicChat,
    AnthropicChatParameters,
    AzureChat,
    BaichuanChat,
    BaichuanChatParameters,
    BailianChat,
    BailianChatParameters,
    DashScopeChat,
    DashScopeChatParameters,
    DashScopeMultiModalChat,
    DashScopeMultiModalChatParameters,
    DeepSeekChat,
    DeepSeekChatParameters,
    HunyuanChat,
    HunyuanChatParameters,
    MinimaxChat,
    MinimaxChatParameters,
    MinimaxProChat,
    MinimaxProChatParameters,
    MoonshotChat,
    MoonshotChatParameters,
    OpenAIChat,
    OpenAIChatParameters,
    WenxinChat,
    WenxinChatParameters,
    YiChat,
    YiChatParameters,
    ZhipuCharacterChat,
    ZhipuCharacterChatParameters,
    ZhipuChat,
    ZhipuChatParameters,
)
from generate.chat_completion.printer import MessagePrinter, SimpleMessagePrinter
from generate.chat_completion.tool import Tool, get_json_schema, tool
from generate.model import ModelParameters

ChatModels: list[tuple[Type[ChatCompletionModel], Type[ModelParameters]]] = [
    (AzureChat, OpenAIChatParameters),
    (AnthropicChat, AnthropicChatParameters),
    (OpenAIChat, OpenAIChatParameters),
    (MinimaxProChat, MinimaxProChatParameters),
    (MinimaxChat, MinimaxProChatParameters),
    (ZhipuChat, ZhipuChatParameters),
    (ZhipuCharacterChat, ZhipuCharacterChatParameters),
    (WenxinChat, WenxinChatParameters),
    (HunyuanChat, HunyuanChatParameters),
    (BaichuanChat, BaichuanChatParameters),
    (BailianChat, BailianChatParameters),
    (DashScopeChat, DashScopeChatParameters),
    (DashScopeMultiModalChat, DashScopeMultiModalChatParameters),
    (MoonshotChat, MoonshotChatParameters),
    (DeepSeekChat, DashScopeChatParameters),
    (YiChat, YiChatParameters),
]

ChatModelRegistry: dict[str, tuple[Type[ChatCompletionModel], Type[ModelParameters]]] = {
    model_cls.model_type: (model_cls, parameter_cls) for model_cls, parameter_cls in ChatModels
}


__all__ = [
    'ChatCompletionModel',
    'RemoteChatCompletionModel',
    'ChatCompletionOutput',
    'ChatCompletionStreamOutput',
    'ModelParameters',
    'AzureChat',
    'MinimaxProChat',
    'MinimaxProChatParameters',
    'MinimaxChat',
    'MinimaxChatParameters',
    'OpenAIChat',
    'OpenAIChatParameters',
    'ZhipuChat',
    'ZhipuChatParameters',
    'ZhipuCharacterChat',
    'ZhipuCharacterChatParameters',
    'WenxinChat',
    'WenxinChatParameters',
    'HunyuanChat',
    'HunyuanChatParameters',
    'BaichuanChat',
    'BaichuanChatParameters',
    'BailianChat',
    'BailianChatParameters',
    'YiChat',
    'YiChatParameters',
    'AnthropicChat',
    'AnthropicChatParameters',
    'DashScopeChat',
    'DashScopeChatParameters',
    'DashScopeMultiModalChat',
    'DashScopeMultiModalChatParameters',
    'MoonshotChat',
    'MoonshotChatParameters',
    'DeepSeekChat',
    'DeepSeekChatParameters',
    'MessagePrinter',
    'SimpleMessagePrinter',
    'get_json_schema',
    'tool',
    'Tool',
    'Prompt',
    'Messages',
    'SystemMessage',
    'UserMessage',
    'AssistantMessage',
    'ToolMessage',
    'FunctionMessage',
    'UserMultiPartMessage',
]
