export function featuresVote() {
    $('.voteUp.callCart').click(function () {
        const _this = $(this);
        const popUpContent = _this.next('.popUpCart').html();

        const popUp = `<div class="popUp" id="popUp">
                        <div class="container">
                            ${popUpContent}
                        </div>
                       </div>`;

        $('body').append(popUp);

        $('.closePopUp').click(function () {
            $('#popUp').remove();
        });
    });
}