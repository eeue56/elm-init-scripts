#!/usr/bin/python

import argparse
import errno
import os
import os.path

api_template = """
module {module_name}.API exposing (main)

import Html exposing (Html)

import {module_name}.Messages exposing (Msg(..))
import {module_name}.Subscriptions exposing (subscriptions)
import {module_name}.Model exposing (Model)
import {module_name}.Update exposing (update)
import {module_name}.View exposing (view)

initialModel : Model
initialModel = {{ }}

init : ( Model, Cmd Msg )
init =
  ( initialModel
  , Cmd.none )

main =
  Html.program
    {{ init = init
    , update = update
    , view = view
    , subscriptions = \_ -> Sub.none }}
""".lstrip()

messages_template = """
module {module_name}.Messages exposing (Msg(..))

type Msg
  = NoOp
""".lstrip()

subscriptions_template = """
module {module_name}.Subscriptions exposing (subscriptions)

import {module_name}.Model exposing (Model)
import {module_name}.Messages exposing (Msg(..))

subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none
""".lstrip()

model_template = """
module {module_name}.Model exposing (Model)

type alias Model =
  {{ }}
""".lstrip()

update_template = """
module {module_name}.Update exposing (update)

import {module_name}.Model exposing (Model)
import {module_name}.Messages exposing (Msg(..))

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    NoOp ->
      (model, Cmd.none)
""".lstrip()

view_template = """
module {module_name}.View exposing (view)

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)

import {module_name}.Model exposing (Model)
import {module_name}.Messages exposing (Msg(..))

view : Model -> Html Msg
view model =
  div [] [ text "Hello world!" ]

""".lstrip()

templates = {
    'API.js.elm': api_template,
    'Messages.elm': messages_template,
    'Subscriptions.elm': subscriptions_template,
    'Model.elm': model_template,
    'Update.elm': update_template,
    'View.elm': view_template
}

def make_boilerplate(module_name, directory, template, file_name):
    file_path = os.path.join(directory, file_name)
    templated = template.format(module_name=module_name)

    with open(file_path, 'w') as f:
        f.write(templated)

def make_boilerplates(module_name, directory, templates):
    for file_name, template in templates.items():
        make_boilerplate(module_name, directory, template, file_name)

def make_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(directory):
            pass
        else:
            raise

def bootstrap(module_name, root_directory):
    directory = os.path.join(root_directory, *module_name.split('.'))

    make_directory(directory)
    make_boilerplates(module_name, directory, templates)

def main():
    parser = argparse.ArgumentParser(description='Initialize an Elm page')

    parser.add_argument('module_name', help='the component name e.g Some.Module.Name')
    parser.add_argument('destination', help='the destination folder. Defaults to current', default="./")
    args = parser.parse_args()

    bootstrap(args.module_name, args.destination)

if __name__ == '__main__':
    main()
