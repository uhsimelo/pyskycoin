# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.25.1
    Contact: contact@skycoin.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'hours': 'int',
        'coins': 'int',
        'uxid': 'str',
        'owner_address': 'str',
        'spent_block_seq': 'int',
        'spent_tx': 'str',
        'time': 'int',
        'src_block_seq': 'int',
        'src_tx': 'str'
    }

    attribute_map = {
        'hours': 'hours',
        'coins': 'coins',
        'uxid': 'uxid',
        'owner_address': 'owner_address',
        'spent_block_seq': 'spent_block_seq',
        'spent_tx': 'spent_tx',
        'time': 'time',
        'src_block_seq': 'src_block_seq',
        'src_tx': 'src_tx'
    }

    def __init__(self, hours=None, coins=None, uxid=None, owner_address=None, spent_block_seq=None, spent_tx=None, time=None, src_block_seq=None, src_tx=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501

        self._hours = None
        self._coins = None
        self._uxid = None
        self._owner_address = None
        self._spent_block_seq = None
        self._spent_tx = None
        self._time = None
        self._src_block_seq = None
        self._src_tx = None
        self.discriminator = None

        if hours is not None:
            self.hours = hours
        if coins is not None:
            self.coins = coins
        if uxid is not None:
            self.uxid = uxid
        if owner_address is not None:
            self.owner_address = owner_address
        if spent_block_seq is not None:
            self.spent_block_seq = spent_block_seq
        if spent_tx is not None:
            self.spent_tx = spent_tx
        if time is not None:
            self.time = time
        if src_block_seq is not None:
            self.src_block_seq = src_block_seq
        if src_tx is not None:
            self.src_tx = src_tx

    @property
    def hours(self):
        """Gets the hours of this InlineResponse200.  # noqa: E501


        :return: The hours of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this InlineResponse200.


        :param hours: The hours of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._hours = hours

    @property
    def coins(self):
        """Gets the coins of this InlineResponse200.  # noqa: E501


        :return: The coins of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._coins

    @coins.setter
    def coins(self, coins):
        """Sets the coins of this InlineResponse200.


        :param coins: The coins of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._coins = coins

    @property
    def uxid(self):
        """Gets the uxid of this InlineResponse200.  # noqa: E501


        :return: The uxid of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._uxid

    @uxid.setter
    def uxid(self, uxid):
        """Sets the uxid of this InlineResponse200.


        :param uxid: The uxid of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._uxid = uxid

    @property
    def owner_address(self):
        """Gets the owner_address of this InlineResponse200.  # noqa: E501


        :return: The owner_address of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this InlineResponse200.


        :param owner_address: The owner_address of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._owner_address = owner_address

    @property
    def spent_block_seq(self):
        """Gets the spent_block_seq of this InlineResponse200.  # noqa: E501


        :return: The spent_block_seq of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._spent_block_seq

    @spent_block_seq.setter
    def spent_block_seq(self, spent_block_seq):
        """Sets the spent_block_seq of this InlineResponse200.


        :param spent_block_seq: The spent_block_seq of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._spent_block_seq = spent_block_seq

    @property
    def spent_tx(self):
        """Gets the spent_tx of this InlineResponse200.  # noqa: E501


        :return: The spent_tx of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._spent_tx

    @spent_tx.setter
    def spent_tx(self, spent_tx):
        """Sets the spent_tx of this InlineResponse200.


        :param spent_tx: The spent_tx of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._spent_tx = spent_tx

    @property
    def time(self):
        """Gets the time of this InlineResponse200.  # noqa: E501


        :return: The time of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse200.


        :param time: The time of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def src_block_seq(self):
        """Gets the src_block_seq of this InlineResponse200.  # noqa: E501


        :return: The src_block_seq of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._src_block_seq

    @src_block_seq.setter
    def src_block_seq(self, src_block_seq):
        """Sets the src_block_seq of this InlineResponse200.


        :param src_block_seq: The src_block_seq of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._src_block_seq = src_block_seq

    @property
    def src_tx(self):
        """Gets the src_tx of this InlineResponse200.  # noqa: E501


        :return: The src_tx of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._src_tx

    @src_tx.setter
    def src_tx(self, src_tx):
        """Sets the src_tx of this InlineResponse200.


        :param src_tx: The src_tx of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._src_tx = src_tx

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
