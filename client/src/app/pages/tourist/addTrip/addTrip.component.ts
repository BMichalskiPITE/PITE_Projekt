import { Component, OnInit } from '@angular/core';
import { Place } from '../../../place';
import { RestService } from '../../../shared/rest.service';
import { AuthService } from '../../../shared/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'add-trip',
  templateUrl: './addTrip.component.html',
  styleUrls: ['./addTrip.component.scss']
})
export class AddTripComponent implements OnInit {

    selectedPlaces:Place[] = [];
    ids:String[] = []
    constructor(private rest:RestService, private auth:AuthService, private router:Router) { }
    tripName = ""
    tripDescription = ""
    ngOnInit() {
    }

    addPlace(place:Place):void {
        if(this.selectedPlaces.indexOf(place, 0) == -1)
            this.selectedPlaces.push(place);
        this.updateIds();
    }

  remove(place):void {
    var index = this.selectedPlaces.indexOf(place, 0);
    if (index > -1) {
       this.selectedPlaces.splice(index, 1);
    }
    this.updateIds();
  }

  updateIds():void {
      this.ids = this.selectedPlaces.map(p => p.placeId);
  }
  registerTrip():void {
      console.log("sggs")
      this.rest.addTrip({
          userId: this.auth.getLoggedUser().id,
          tripName: this.tripName,
          tripDescription: this.tripDescription,
          places: this.ids
      }).then(i => {
          this.router.navigate(['/tourist/tripDetails/'+i.tripId]);
        })
  }
}
