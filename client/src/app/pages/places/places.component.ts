import { Component, OnInit } from '@angular/core';
import { PlacesService } from '../../places.service'
import { Place } from '../../place'

@Component({
  selector: 'places',
  templateUrl: './places.component.html',
  styleUrls: ['./places.component.scss']
})
export class PlacesComponent implements OnInit {

  places: Place[];

  constructor(private placesService: PlacesService) { }

  ngOnInit() {
    this.showPlaces();
  }

  showPlaces() {
    this.placesService.getPlaces()
      .then(data => { 
        this.places = data;
      });
  }

}
