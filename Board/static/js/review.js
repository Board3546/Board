const user_review = document.querySelector('#id_user');
const message_review = document.querySelector('#id_message');

$(function ($) {
    $('#review-form').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                $('.alert-success').text(response.ok_message).removeClass('d-none');
                user_review.value = '';
                message_review.value = '';
                setTimeout(() => $('.alert-success').addClass('d-none'), 5000);
            },
            error: function (response) {
                if (response.status === 400) {
                    $('.alert-danger').text(response.responseJSON.error).removeClass('d-none')
                }
            }
        })

    })
})