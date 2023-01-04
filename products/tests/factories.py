import factory

from products.models import Product, Specification, ProductsSpecifications, ProductImage, ProductVideo


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("slug")
    short_description = factory.Faker("sentence", nb_words=5)
    description = factory.Faker("paragraph", nb_sentences=5)
    price = factory.Faker("pyint")
    image = factory.django.ImageField()

    @factory.post_generation
    def images(self, _, extracted: int, **kwargs) -> None:
        assert isinstance(extracted, int)
        return ProductImageFactory.create_batch(extracted, product=self)

    @factory.post_generation
    def videos(self, _, extracted: int, **kwargs) -> None:
        assert isinstance(extracted, int)
        return ProductVideoFactory.create_batch(extracted, product=self)


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    image = factory.django.ImageField()
    product = factory.SubFactory(ProductFactory)


class ProductVideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductVideo

    video = factory.django.FileField()
    product = factory.SubFactory(ProductFactory)


class SpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Specification

    image = factory.django.ImageField()


class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductsSpecifications

    product = factory.SubFactory(ProductFactory)
    specification = factory.SubFactory(SpecificationFactory)
    value = 1


class ProductWithSpecificationFactory(ProductFactory):
    specifications = factory.RelatedFactory(
        ProductSpecificationFactory,
        factory_related_name="product",
    )
