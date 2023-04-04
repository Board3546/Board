from questionnaire.models import Service


def services_count(context):
    services = Service.objects.filter(owner=context.get("profile"))
    context["services_women"] = services.filter(type=1).prefetch_related("images")
    context["services_massage"] = services.filter(type=2).prefetch_related("images")
    context["services_men"] = services.filter(type=3).prefetch_related("images")
    context["services_company"] = services.filter(type=4).prefetch_related("images")
    c1 = c2 = c3 = c4 = 0
    for service in services:
        if service.type == 1:
            c1 += 1
        elif service.type == 2:
            c2 += 1
        elif service.type == 3:
            c3 += 1
        else:
            c4 += 1
    context["service_women_count"] = c1
    context["service_massage_count"] = c2
    context["service_men_count"] = c3
    context["service_company_count"] = c4
    return context
