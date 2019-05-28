import 'chart.js/dist/Chart';

export function webStats() {
    $.ajax({
        type: 'get',
        url: '/api/stats/',
        async: true,
        dataType: 'json',
        success: (response) => {

            const statusColorSet = ['#B71C1C', '#001A23', '#436436'];

            setChart('featuresStatuses', 'pie', iterateObject(response,
                'features', 'Feature progress'), statusColorSet);

            setChart('bugsStatuses', 'pie', iterateObject(response,
                'bugs', 'Bug progress'), statusColorSet);

            let colors = ['#436436', '#3c5a31', '#36502b', '#2f4626', '#283c20', '#22321b',
                '#1b2816', '#141e10', '#0d140b', '#070a05', '#000000'];


            setChart('featuresVoted', 'bar', {
                labels: response['votes']['features']['labels'],
                data: response['votes']['features']['votes'],
                label_name: 'Most voted feature'
            }, colors);


            colors = ['#b71c1c', '#a51919', '#921616', '#801414', '#6e1111', '#5c0e0e', '#490b0b',
                '#370808', '#250606', '#120303', '#000000'];

            setChart('bugsVoted', 'bar', {
                labels: response['votes']['bugs']['labels'],
                data: response['votes']['bugs']['votes'],
                label_name: 'Most voted bug'
            }, colors);

        },
        error: (error) => {
            console.error(error);
        }
    });
}


function iterateObject(response, type, label_name) {
    const statuses = {
        labels: [],
        data: [],
        label_name: label_name
    };

    Object.keys(response['statuses'][type]).forEach((key) => {
        statuses.labels.push(key);
        statuses.data.push(response['statuses'][type][key]);
    });

    return statuses;
}


function setChart(chartID, chartType, data, colors = []) {
    const ctx = document.getElementById(chartID).getContext('2d');
    new Chart(ctx, {
        type: chartType,
        data: {
            labels: data['labels'],
            datasets: [{
                label: data['label_name'],
                data: data['data'],
                backgroundColor: colors
            }]
        }
    });
}