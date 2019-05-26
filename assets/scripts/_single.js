export function singlePostActions() {
    // confirmation deletion
    $('#deletePost').click(function () {
        $(this).hide();

        $('.deletionConfirm').fadeIn(100);
    });

    $('#cancelDeletion').click(function () {
        $('.deletionConfirm').hide();
        $('#deletePost').fadeIn(100);
    });
}