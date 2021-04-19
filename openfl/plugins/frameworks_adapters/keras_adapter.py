class FrameworkAdapterPlugin:
    def __init__(self) -> None:
        pass
        

    @staticmethod
    def get_tensor_dict(model, optimizer=None, suffix=''):
        model_weights = _get_weights_dict(model, suffix)

        if optimizer is not None:
            opt_weights = _get_weights_dict(optimizer, suffix)

            model_weights.update(opt_weights)
            if len(opt_weights) == 0:
                # ToDo: warn user somehow
                pass

        return model_weights

    @staticmethod
    def set_tensor_dict(model, tensor_dict, optimizer=None, device='cpu'):
        """
        Set the model weights with a tensor dictionary.

        Args:
            tensor_dict: the tensor dictionary
            with_opt_vars (bool): True = include the optimizer's status.
        """
        model_weight_names = [weight.name for weight in model.weights]
        model_weights_dict = {
            name: tensor_dict[name] for name in model_weight_names
        }
        _set_weights_dict(model, model_weights_dict)

        if optimizer is not None:
            opt_weight_names = [
                weight.name for weight in optimizer.weights
            ]
            opt_weights_dict = {
                name: tensor_dict[name] for name in opt_weight_names
            }
            _set_weights_dict(optimizer, opt_weights_dict)



def _get_weights_dict(obj, suffix=''):
    """
    Get the dictionary of weights.

    Parameters
    ----------
    obj : Model or Optimizer
        The target object that we want to get the weights.

    Returns
    -------
    dict
        The weight dictionary.
    """
    weights_dict = {}
    weight_names = [weight.name for weight in obj.weights]
    weight_values = obj.get_weights()
    for name, value in zip(weight_names, weight_values):
        weights_dict[name + suffix] = value
    return weights_dict


def _set_weights_dict(obj, weights_dict):
    """Set the object weights with a dictionary.

    The obj can be a model or an optimizer.

    Args:
        obj (Model or Optimizer): The target object that we want to set
        the weights.
        weights_dict (dict): The weight dictionary.

    Returns:
        None
    """
    weight_names = [weight.name for weight in obj.weights]
    weight_values = [weights_dict[name] for name in weight_names]
    obj.set_weights(weight_values)