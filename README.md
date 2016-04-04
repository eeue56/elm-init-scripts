# elm-init-scripts


This is a script to bootstrap your projects in the style that NRI use internally

## Usage:

```bash

python bootstrap.py Some.Module.Name app/assets/javascripts/

```

Should generate the following files:

app/assets/javascripts/Some/Module/Name/API.js.elm
```elm
module Some.Module.Name.API where

import Html exposing (Html)
import StartApp
import Effects exposing (Never)
import Task exposing (Task)

import Some.Module.Name.Update exposing (update, Action(..), Addresses)
import Some.Module.Name.Model exposing (Model)
import Some.Module.Name.View exposing (view)


app : StartApp.App Model
app =
    let
        initModel : Model
        initModel =
            { }

        modelWithEffects =
            (initModel, Effects.none)

        addresses =
            { }
    in
        StartApp.start
            { init = modelWithEffects
            , view = view
            , update = (update addresses)
            , inputs = [ ]
            }

main : Signal Html
main =
    app.html

port authToken : String

port tasks : Signal (Task.Task Never ())
port tasks =
    app.tasks

```
app/assets/javascripts/Some/Module/Name/Update.elm
```elm
module Some.Module.Name.Update where

import Effects exposing (Effects)
import Some.Module.Name.Model exposing (..)

type Action
  = NoOp

type alias Addresses =
  {}

update : Addresses -> Action -> Model -> (Model, Effects.Effects Action)
update addresses action model =
  case action of
    NoOp ->
      (model, Effects.none)
```
app/assets/javascripts/Some/Module/Name/Model.elm
```elm
module Some.Module.Name.Model where

type alias Model =
  {}
```
app/assets/javascripts/Some/Module/Name/View.elm
```elm
module Some.Module.Name.View (..) where

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Signal

import Some.Module.Name.Model exposing (..)
import Some.Module.Name.Update exposing (..)


view : Signal.Address Action -> Model -> Html
view address model =
  div [] [ text "Hello world!" ]


```
