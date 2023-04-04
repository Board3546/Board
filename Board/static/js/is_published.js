const disable_showing = document.querySelector('#disable_showing');
const enable_showing = document.querySelector('#enable_showing');
let service_id = document.querySelector('#service_id');

$(function ($) {
    $('#publish-form').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: "POST",
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
$(function ($) {
    $('#unpublish-form').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: "POST",
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                $('.alert-success').text(response.ok_message).removeClass('d-none');
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