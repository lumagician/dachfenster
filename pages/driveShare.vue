<template>
  <v-row justify='center' align='center'>
    <v-col cols='12' sm='8' md='6'>
      <v-card>
        <v-card-title class='headline'>
          {{ title }}
        </v-card-title>
        <v-card-text class='text-left'>
          <div v-for='weekday in weekDays'>
            <input type='checkbox' :id='weekday.id' v-model='weekday.selected'>
            <label :for='weekday.id'>{{ weekday.label }}</label>
          </div>
          <div class='{ display:inline-block}' style='margin-top: 10px;'>
            <select v-model='selectedFromTo'  :style="{color: 'white', 'border-style': 'solid', 'border-color': 'primary'}">
              <option disabled value=''></option>
              <option :style="{color: 'black'}">Ab</option>
              <option :style="{color: 'black'}">An</option>
            </select>
            <input type="time" id="fromtotime" name="fromtotime"  v-model='time'  class=" inputValue"
                    required>
            <div class='{ display:inline-block}' style='margin-top: 10px;'><b>Regelmässigkeit: </b>
              <select v-model='selected' :style="{color: 'white', 'border-style': 'solid', 'border-color': 'primary'}">
                <option disabled value=''></option>
                <option :style="{color: 'black'}">wöchentlich</option>
              </select>
            </div>
          </div>
        </v-card-text>
        <v-card-text>
          <p>
            <button class='fieldFromTo'>Von</button>
            <input type='text' name='street' id='fromAdress' v-model='fromAddress' class='inputValueFromTo inputValue'><br>
            <button class='fieldFromTo'>Nach</button>
            <input type='text' name='street' id='toAdress' v-model='toAddress' class='inputValueFromTo inputValue'>
          </p>
          <v-btn color='primary' v-on:click='searchRoutes'>Sharen</v-btn>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>


export default {

  data() {
    return {
      title: 'Fahrt sharen',
      checked: true,
      timePicker: '',
      selected: '',
      selectedFromTo: 'Ab',
      time: '',
      weekDays: [
        {
          id: 'monday',
          selected: false,
          label: 'Montag'
        },
        {
          id: 'tuesday',
          selected: false,
          label: 'Dienstag'
        },
        {
          id: 'wednersday',
          selected: false,
          label: 'Mittwoch'
        },
        {
          id: 'thursday',
          selected: false,
          label: 'Donnerstag'
        },
        {
          id: 'friday',
          selected: false,
          label: 'Freitag'
        },
        {
          id: 'saturday',
          selected: false,
          label: 'Samstag'
        },
        {
          id: 'sunday',
          selected: false,
          label: 'Sonntag'
        }
      ],
      fromAddress: 'Guisanstr. 2, 3014 Bern',
      toAddress: 'Maritzstrasse 20, 3400 Burgdorf'

    }
  }
}
</script>
