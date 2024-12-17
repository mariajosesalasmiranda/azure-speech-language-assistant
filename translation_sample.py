#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Translation recognition samples for the Microsoft Cognitive Services Speech SDK
"""

import time

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)

# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "4L95rUetZClDjVWMkZiDENE7ju1Oka8IHpXTDLZTcyd63x2zxJlMJQQJ99ALACHYHv6XJ3w3AAAAACOG3REc", "eastus2"

# Specify the path to audio files containing speech (mono WAV / PCM with a sampling rate of 16
# kHz).
weatherfilename = "whatstheweatherlike.wav"
multilingual_wav_file = "en-us_zh-cn.wav"


def translation_once_from_mic():
    """performs one-shot speech translation from input from the default microphone"""
    # <TranslationOnceWithMic>
    # set up translation parameters: source language and target languages
    translation_config = speechsdk.translation.SpeechTranslationConfig(
        subscription=speech_key, region=service_region,
        speech_recognition_language='en-US',
        target_languages=('de', 'fr', 'zh-Hans'))
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # Creates a translation recognizer using and audio file as input.
    recognizer = speechsdk.translation.TranslationRecognizer(
        translation_config=translation_config, audio_config=audio_config)

    # Starts translation, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of about 30
    # seconds of audio is processed. It returns the recognized text as well as the translation.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    print("Parla ora... (sto ascoltando)")
    result = recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("""Recognized: {}
        German translation: {}
        French translation: {}
        Chinese translation: {}""".format(
            result.text, result.translations['de'],
            result.translations['fr'],
            result.translations['zh-Hans'],))
    elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        print("Translation canceled: {}".format(result.cancellation_details.reason))
        if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(result.cancellation_details.error_details))
    # </TranslationOnceWithMic>

translation_once_from_mic()
