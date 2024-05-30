# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.user import User  # noqa: F401,E501
from swagger_server import util


class Payment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, user: User=None, amount: int=None):  # noqa: E501
        """Payment - a model defined in Swagger

        :param id: The id of this Payment.  # noqa: E501
        :type id: int
        :param user: The user of this Payment.  # noqa: E501
        :type user: User
        :param amount: The amount of this Payment.  # noqa: E501
        :type amount: int
        """
        self.swagger_types = {
            'id': int,
            'user': User,
            'amount': int
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'amount': 'amount'
        }
        self._id = id
        self._user = user
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'Payment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Payment of this Payment.  # noqa: E501
        :rtype: Payment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Payment.


        :return: The id of this Payment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Payment.


        :param id: The id of this Payment.
        :type id: int
        """

        self._id = id

    @property
    def user(self) -> User:
        """Gets the user of this Payment.


        :return: The user of this Payment.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user: User):
        """Sets the user of this Payment.


        :param user: The user of this Payment.
        :type user: User
        """

        self._user = user

    @property
    def amount(self) -> int:
        """Gets the amount of this Payment.


        :return: The amount of this Payment.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this Payment.


        :param amount: The amount of this Payment.
        :type amount: int
        """

        self._amount = amount