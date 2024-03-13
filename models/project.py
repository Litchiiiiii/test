# coding: utf-8

"""
    ParaTranz OpenAPI 文档

    本文档介绍 ParaTranz.cn 平台的 API ## 获取 Token 首先需要获取API Token，可以通过点击个人资料页面左侧的小钥匙图标获取API Token， 调用 API 时将 Token 直接放在请求头的 Authorization 中即可。  cURL 使用示例:      $ curl --header \"Authorization: XXXXXXXXX\" https://paratranz.cn/api/projects  ## 频率限制 每分钟120次调用，超出后将会降速（增加延迟），1分钟后自动恢复。 ## 错误处理 API 返回的错误格式如下      {       \"message\": \"ERROR MESSAGE\", // 错误消息       \"code\": 10000 // 5位错误代码，注意与下面的HTTP状态码区分，部分接口不返回     }  HTTP状态码有以下几种类型   * 400 - 调用参数错误   * 401 - Token 错误或过期   * 403 - 没有相关权限   * 404 - 资源不存在   * 405 - 没有相关HTTP方法，一般为调用方法错误   * 429 - 调用过于频繁，具体频率限制请看上一节   * 500 - 服务器错误，一般会提供具体出错的位置，请发送给站长方便定位问题   * 502 - 服务器无响应，部分用户被墙时可能会遇到   * 503 - 服务不可用   * 504 - 服务超时，访问量大时会出现  ## SDK 及 JSON 格式的 API 文档 本文档遵循 OpenAPI 规范，[点击此处](https://paratranz.cn/api-docs?raw=1) 获取 JSON 格式的文档，您可以使用 [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) 生成各种语言的 SDK ## 更新历史   * v0.3.5 - 2023.12.25 修复部分 schema 问题   * v0.3.4 - 2023.12.23 增加API调用频率限制说明   * v0.3.3 - 2023.08.11 增加项目成员相关接口说明   * v0.3.2 - 2022.11.04 增加文件翻译相关接口说明   * v0.3.1 - 2022.10.16 修改 tag 及 schema 以便生成 sdk   * v0.3.0 - 2022.10.16 增加术语历史记录接口说明，调整历史记录接口字段; 增加文档中 operationId 定义;                         修复项目信息相关接口格式定义; 增加 JSON 格式文档入口   * v0.2.1 - 2022.07.23 增加成员贡献接口文档; 完善列表接口数据结构   * v0.2.0 - 2022.06.15 增加讨论及私信相关接口文档   * v0.1.3 - 2022.03.10 增加历史记录相关接口文档   * v0.1.2 - 2022.02.07 完善词条搜索接口 query 参数说明   * v0.1.1 - 2022.01.17 增加文件历史相关接口文档   * v0.1.0 - 2022.01.12 初次发布 

    The version of the OpenAPI document: 0.3.4
    Contact: master@mail.paratranz.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Project(BaseModel):
    """
    项目
    """ # noqa: E501
    id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    uid: Optional[StrictInt] = Field(default=None, description="所有者用户ID")
    user: Optional[Dict[str, Any]] = Field(default=None, description="所有者用户信息")
    name: Optional[StrictStr] = Field(default=None, description="项目名称")
    logo: Optional[StrictStr] = Field(default=None, description="项目LOGO链接")
    desc: Optional[StrictStr] = Field(default=None, description="项目说明")
    source: Optional[StrictStr] = Field(default=None, description="源语言")
    dest: Optional[StrictStr] = Field(default=None, description="目标语言")
    members: Optional[StrictInt] = Field(default=None, description="成员数量")
    game: Optional[StrictStr] = Field(default=None, description="所属游戏")
    license: Optional[StrictStr] = Field(default=None, description="项目使用的许可证")
    active_level: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="项目活跃度", alias="activeLevel")
    stage: Optional[StrictInt] = Field(default=None, description="项目状态")
    privacy: Optional[StrictInt] = Field(default=None, description="项目隐私状态 * 0 - 公开 * 1 - 内部（项目公开但动态及文件私密） * 2 - 私密 ")
    download: Optional[StrictInt] = Field(default=None, description="下载权限 * 0 - 公开 * 1 - 内部 * 2 - 私密 ")
    issue_mode: Optional[StrictInt] = Field(default=None, description="讨论权限 * 0 - 公开（所有用户都可以创建及加入讨论） * 1 - 内部（仅项目成员可以创建讨论但所有用户都可以加入） * 2 - 私密（仅项目成员可以创建及加入讨论） ", alias="issueMode")
    review_mode: Optional[StrictInt] = Field(default=None, description="校对等级 * 0 - 无须校对 * 1 - 一次校对 * 2 - 二次校对 ", alias="reviewMode")
    join_mode: Optional[StrictInt] = Field(default=None, description="加入方式 * 0 - 公开（所有用户都可以直接加入项目） * 1 - 申请（加入项目需提交申请） * 2 - 测试（加入项目需完成测试） * 3 - 私密（仅管理员可添加成员） ", alias="joinMode")
    __properties: ClassVar[List[str]] = ["id", "createdAt", "updatedAt", "uid", "user", "name", "logo", "desc", "source", "dest", "members", "game", "license", "activeLevel", "stage", "privacy", "download", "issueMode", "reviewMode", "joinMode"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Project from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "created_at",
                "updated_at",
                "uid",
                "user",
                "members",
                "license",
                "active_level",
                "stage",
            },
            exclude_none=True,
        )
        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Project from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "uid": obj.get("uid"),
            "user": obj.get("user"),
            "name": obj.get("name"),
            "logo": obj.get("logo"),
            "desc": obj.get("desc"),
            "source": obj.get("source"),
            "dest": obj.get("dest"),
            "members": obj.get("members"),
            "game": obj.get("game"),
            "license": obj.get("license"),
            "activeLevel": obj.get("activeLevel"),
            "stage": obj.get("stage"),
            "privacy": obj.get("privacy"),
            "download": obj.get("download"),
            "issueMode": obj.get("issueMode"),
            "reviewMode": obj.get("reviewMode"),
            "joinMode": obj.get("joinMode")
        })
        return _obj


