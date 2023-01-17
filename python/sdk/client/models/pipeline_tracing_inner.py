# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PipelineTracingInner(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'operation_type': 'str',
        'specs': 'FreeFormObject',
        'inputs': 'FreeFormObject',
        'outputs': 'FreeFormObject'
    }

    attribute_map = {
        'operation_type': 'operation_type',
        'specs': 'specs',
        'inputs': 'inputs',
        'outputs': 'outputs'
    }

    def __init__(self, operation_type=None, specs=None, inputs=None, outputs=None):  # noqa: E501
        """PipelineTracingInner - a model defined in Swagger"""  # noqa: E501
        self._operation_type = None
        self._specs = None
        self._inputs = None
        self._outputs = None
        self.discriminator = None
        if operation_type is not None:
            self.operation_type = operation_type
        if specs is not None:
            self.specs = specs
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs

    @property
    def operation_type(self):
        """Gets the operation_type of this PipelineTracingInner.  # noqa: E501


        :return: The operation_type of this PipelineTracingInner.  # noqa: E501
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this PipelineTracingInner.


        :param operation_type: The operation_type of this PipelineTracingInner.  # noqa: E501
        :type: str
        """

        self._operation_type = operation_type

    @property
    def specs(self):
        """Gets the specs of this PipelineTracingInner.  # noqa: E501


        :return: The specs of this PipelineTracingInner.  # noqa: E501
        :rtype: FreeFormObject
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """Sets the specs of this PipelineTracingInner.


        :param specs: The specs of this PipelineTracingInner.  # noqa: E501
        :type: FreeFormObject
        """

        self._specs = specs

    @property
    def inputs(self):
        """Gets the inputs of this PipelineTracingInner.  # noqa: E501


        :return: The inputs of this PipelineTracingInner.  # noqa: E501
        :rtype: FreeFormObject
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this PipelineTracingInner.


        :param inputs: The inputs of this PipelineTracingInner.  # noqa: E501
        :type: FreeFormObject
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this PipelineTracingInner.  # noqa: E501


        :return: The outputs of this PipelineTracingInner.  # noqa: E501
        :rtype: FreeFormObject
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this PipelineTracingInner.


        :param outputs: The outputs of this PipelineTracingInner.  # noqa: E501
        :type: FreeFormObject
        """

        self._outputs = outputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PipelineTracingInner, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PipelineTracingInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other