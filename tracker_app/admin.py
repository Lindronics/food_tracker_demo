from django.contrib import admin
from tracker_app.models import Day, Food, FoodLog, FoodAmount, Meal, MealLog


class DayAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', )


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'fat', 'carbs', 'protein', )


class FoodLogAdmin(admin.ModelAdmin):
    list_display = ('food_amount', 'day', 'timestamp', )


class FoodAmountAdmin(admin.ModelAdmin):
    list_display = ('food', 'amount', )


class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_description', )


class MealLogAdmin(admin.ModelAdmin):
    list_display = ('meal', 'amount', 'day', 'timestamp', )


admin.site.register(Day, DayAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodLog, FoodLogAdmin)
admin.site.register(FoodAmount, FoodAmountAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(MealLog, MealLogAdmin)
