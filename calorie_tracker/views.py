from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models import Sum
from django.utils import timezone
from django.contrib import messages
from .models import FoodItem
from .forms import FoodItemForm


def index(request):
    """
    Main View:
    - Lists all food items recorded for today.
    - Handles creation of new food items.
    - Computes daily aggregate calorie total.
    """
    today = timezone.now().date()
    today_items = FoodItem.objects.filter(date_added__date=today)
    
    # Calculate daily aggregate total
    total_calories = today_items.aggregate(total=Sum('calories'))['total'] or 0

    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food item added successfully!')
            return redirect('calorie_tracker:index')
        else:
            messages.error(request, 'Error adding food item. Please check inputs.')
    else:
        form = FoodItemForm()

    context = {
        'items': today_items,
        'total_calories': total_calories,
        'form': form,
        'today_date': today,
    }
    return render(request, 'calorie_tracker/index.html', context)


@require_POST
def delete_food_item(request, item_id):
    """
    Deletes a single food item by ID.
    Restricted to POST requests for security.
    """
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    messages.info(request, f'"{item.name}" removed.')
    return redirect('calorie_tracker:index')


@require_POST
def reset_daily_calories(request):
    """
    Clears all food item entries for the current calendar day.
    Restricted to POST requests for security.
    """
    today = timezone.now().date()
    deleted_count, _ = FoodItem.objects.filter(date_added__date=today).delete()
    messages.warning(request, f'Daily count reset! Deleted {deleted_count} item(s).')
    return redirect('calorie_tracker:index')