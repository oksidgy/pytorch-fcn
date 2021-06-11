import torchvision


def VGG16(pretrained=False):
    model = torchvision.models.vgg16(pretrained=pretrained)

    return model