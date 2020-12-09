import torch

trained_model_name = 'best.pt'


def loaded_trained_model(model_name):
    trained_model = torch.load(model_name)
    return trained_model


def predict_image(image_name, trained_model):
    pass


if __name__ == '__main__':
    loaded_model = loaded_trained_model(trained_model_name)
    images_to_predict = []
    for image_name in images_to_predict:
        predict_image(image_name, loaded_model)
