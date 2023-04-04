from django.core.exceptions import ObjectDoesNotExist

from questionnaire.models import MultipleImage, Addition


def save_images(request, service):
    """Save images from request.FILES to service"""
    for image in request.FILES.getlist("images"):
        MultipleImage.objects.create(image=image, service=service)


def save_additions(request, object):
    """Save additions from request.POST to service"""
    added_additions = []
    additions = Addition.objects.all()
    additions_count = Addition.objects.all().count()
    for addition_id in range(1, additions_count + 1):
        if f"additions_{addition_id}" in request.POST:
            addition_price = (
                int(request.POST[f"price_{addition_id}"])
                if request.POST[f"price_{addition_id}"] != ""
                else 0
            )
            try:
                current_addition = Addition.objects.get(
                    pk=addition_id, price=addition_price
                )
            except ObjectDoesNotExist:
                expected_addition = additions.get(pk=addition_id)
                current_addition = Addition.objects.create(
                    title=expected_addition.title,
                    category=expected_addition.category,
                    price=addition_price,
                )
            added_additions.append(current_addition.id)
    additions_for_object = Addition.objects.filter(id__in=added_additions)
    object.additions.set(additions_for_object)
    object.save()
