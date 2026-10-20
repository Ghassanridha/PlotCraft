// فتح نافذة الاشتراكات
function openSubscriptionModal() {
    const modal = document.getElementById('subscriptionModal');
    if (modal) {
        modal.classList.remove('hidden');
    }
}

// فتح النافذة عند الضغط من الأزرار التي تعتمد openSubscriptionModalFromBadge
function openSubscriptionModalFromBadge(event) {
    if (event) event.stopPropagation();
    openSubscriptionModal();
}

// إغلاق نافذة الاشتراكات
function closeSubscriptionModal() {
    const modal = document.getElementById('subscriptionModal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

// اختيار الخطة عند الضغط عليها
function selectPlan(element) {
    document.querySelectorAll('.plan-card').forEach(card => card.classList.remove('selected'));
    element.classList.add('selected');
}

// تأكيد الاشتراك
function confirmSubscription() {
    if (typeof showToast === 'function') {
        showToast('جاري التوجيه لبوابة الدفع...');
    }
    setTimeout(() => {
        closeSubscriptionModal();
    }, 1200);
}
