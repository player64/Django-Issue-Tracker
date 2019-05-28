import '../styles/main.scss';
import './common';
import {checkout} from './_checkout';
import {featuresVote} from "./_features";
import {singlePostActions} from './_single';
import {webStats} from './_stats';

const _body = $('body');

if (_body.hasClass('single_posts')) {
    singlePostActions();
}

if (_body.hasClass('features')) {
    featuresVote();
}

if (_body.hasClass('checkout')) {
    checkout();
}

if (_body.hasClass('stats')) {
    webStats();
}