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
module Some.Module.Name.API exposing (main)

import Html exposing (Html)

import Some.Module.Name.Messages exposing (Msg(..))
import Some.Module.Name.Subscriptions exposing (subscriptions)
import Some.Module.Name.Model exposing (Model)
import Some.Module.Name.Update exposing (update)
import Some.Module.Name.View exposing (view)

initialModel : Model
initialModel = { }

init : ( Model, Cmd Msg )
init =
  ( initialModel
  , Cmd.none )

main =
 Html.program
   { init = init
   , update = update
   , view = view
   , subscriptions = \_ -> Sub.none }
```
app/assets/javascripts/Some/Module/Name/Update.elm
```elm
module Some.Module.Name.Update exposing (update)

import Some.Module.Name.Model exposing (Model)
import Some.Module.Name.Messages exposing (Msg(..))

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    NoOp ->
      (model, Cmd.none)
```
app/assets/javascripts/Some/Module/Name/Model.elm
```elm
module Some.Module.Name.Model where

type alias Model =
  {}
```
app/assets/javascripts/Some/Module/Name/View.elm
```elm
module Some.Module.Name.View exposing (view)

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)

import Some.Module.Name.Model exposing (Model)
import Some.Module.Name.Messages exposing (Msg(..))

view : Model -> Html Msg
view model =
  div [] [ text "Hello world!" ]
```
app/assets/javascripts/Some/Module/Name/Messages.elm
```elm
module Some.Module.Name.Messages exposing (Msg(..))

type Msg
  = NoOp
```
app/assets/javascripts/Some/Module/Name/Subscriptions.elm
```elm
module Some.Module.Name.Subscriptions exposing (subscriptions)

import Some.Module.Name.Model exposing (Model)
import Some.Module.Name.Messages exposing (Msg(..))

subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none
```
