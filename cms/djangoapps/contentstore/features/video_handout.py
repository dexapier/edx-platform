# -*- coding: utf-8 -*-
# disable missing docstring
# pylint: disable=C0111

from lettuce import world, step
from nose.tools import assert_true # pylint: disable=E0611
from video_editor import RequestHandlerWithSessionId, success_upload_file


@step('I (?:upload|replace) handout file(?: by)? "([^"]*)"$')
def upload_handout(step, filename):
    world.css_click('.wrapper-comp-setting.file-uploader .upload-action')
    success_upload_file(filename)


@step('I can download handout file( in editor)?$')
def i_can_download_handout(_step, is_editor):
    if is_editor:
        selector = '.wrapper-comp-setting.file-uploader .download-action'
    else:
        selector = '.video-handout.video-download-button a'

    button = world.css_find(selector).first
    url = button['href']
    request = RequestHandlerWithSessionId()
    assert_true(request.get(url).is_success())


@step('I can download handout file( in editor)? with mime type "([^"]*)"$')
def i_can_download_handout_with_mime_type(_step, is_editor, mime_type):
    if is_editor:
        selector = '.wrapper-comp-setting.file-uploader .download-action'
    else:
        selector = '.video-handout.video-download-button a'

    button = world.css_find(selector).first
    url = button['href']
    request = RequestHandlerWithSessionId()
    assert_true(request.get(url).is_success())
    assert_true(request.check_header('content-type', mime_type))


@step('I clear handout$')
def clear_heandout(_step):
    world.css_click('.wrapper-comp-setting.file-uploader .setting-clear')
