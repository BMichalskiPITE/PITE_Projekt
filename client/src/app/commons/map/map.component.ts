import { Component, ViewChild, OnInit, EventEmitter, Output, Input } from '@angular/core';
import { AgmMap } from '@agm/core';
import { PlacesService } from '../../places.service'; 
import { Place } from  '../../place';

@Component({
  selector: 'mapbf',
  styleUrls: ['./map.component.scss'],
  templateUrl: './map.component.html'
})
export class MapComponent implements OnInit {

  @Output() onSelect = new EventEmitter<Place>();
  @Input() selectedIds:string[] = [];
  @Input() places: Place[];
  @Input() selectable:Boolean = false;
  constructor(private placesService: PlacesService) { }

  ngOnInit() {
    if(!this.places)
      this.showPlaces();
  }

  showPlaces() {
    this.placesService.getPlaces()
      .then(
        data => { 
        this.places = data;
      }).catch(
      error => alert('Error when loading data: ' + JSON.stringify(error))
    );
  }
  
  isSelected(place:Place):boolean {
    return this.selectedIds.indexOf(place.placeId,0) !== -1;
  }

  @ViewChild(AgmMap)
  public agmMap: AgmMap
  
  lat = 50.0645311;
  lng = 19.9371252;

  selectPlace(place:Place):void {
    this.onSelect.emit(place);
  }
  opened(o):boolean {
    return this.places.findIndex(e => e==o) < 5;
  }
}


class MapObject{
  latitude:number;
  longitude:number;
  photoRef:string;
  name:string;
  placeId:string;
  vicinty:string;
}