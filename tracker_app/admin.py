from django.contrib import admin
from tracker_app.models import Food, FoodLog, FoodAmount, Meal, MealLog


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'fat', 'carbs', 'protein', )


class FoodLogAdmin(admin.ModelAdmin):
    list_display = ('food', 'amount', 'day', 'timestamp', 'user', )


class FoodAmountAdmin(admin.ModelAdmin):
    list_display = ('food', 'amount', )


class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_description', )


class MealLogAdmin(admin.ModelAdmin):
    list_display = ('meal', 'amount', 'day', 'timestamp', 'user', )


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodLog, FoodLogAdmin)
admin.site.register(FoodAmount, FoodAmountAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(MealLog, MealLogAdmin)
