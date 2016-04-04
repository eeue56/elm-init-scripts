import argparse
import errno
import os
import os.path

api_template = """
module {module_name}.API where

import Html exposing (Html)
import StartApp
import Effects exposing (Never)
import Task exposing (Task)

import {module_name}.Update exposing (update, Action(..), Addresses)
import {module_name}.Model exposing (Model)
import {module_name}.View exposing (view)


app : StartApp.App Model
app =
    let
        initModel : Model
        initModel =
            {{ }}

        modelWithEffects =
            (initModel, Effects.none)

        addresses =
            {{ }}
    in
        StartApp.start
            {{ init = modelWithEffects
            , view = view
            , update = (update addresses)
            , inputs = [ ]
            }}

main : Signal Html
main =
    app.html

port authToken : String

port tasks : Signal (Task.Task Never ())
port tasks =
    app.tasks
""".lstrip()

model_template = """
module {module_name}.Model where

type alias Model =
  {{ }}
""".lstrip()

update_template = """
module {module_name}.Update where

import Effects exposing (Effects)
import {module_name}.Model exposing (..)

type Action
  = NoOp

type alias Addresses =
  {{ }}

update : Addresses -> Action -> Model -> (Model, Effects.Effects Action)
update addresses action model =
  case action of
    NoOp ->
      (model, Effects.none)
""".lstrip()

view_template = """
module {module_name}.View (..) where

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Signal

import {module_name}.Model exposing (..)
import {module_name}.Update exposing (..)


view : Signal.Address Action -> Model -> Html
view address model =
  div [] [ text "Hello world!" ]
""".lstrip()

templates = {
    'API.js.elm': api_template,
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
