import { Component, OnInit } from '@angular/core';
import { Place } from '../../../place';
import { Router } from '@angular/router';
import { AuthService } from '../../../shared/auth.service';
import { RestService } from '../../../shared/rest.service';


@Component({
  selector: 'all-trips',
  templateUrl: './allTrips.component.html',
  styleUrls: ['./allTrips.component.scss']
})
export class AllTripsComponent implements OnInit {

    trips = [
        {
            tripId: "21",
            tripName: "nazwa mojej superowej  wycieczkie",
            tripDescription: "Opis jakiegos miejsca, ktory ktos sobie dodał",
            place: {
                name: "nazwa miejsca 1",
                photoref: "CmRaAAAAEnf6pOTUJdMv0aC-5ukwXNY74FKVl-kPCEmnhX-eSodHY3ZKukK5170GUfwlrHnGj3IDhNoeqWeFe0hlDVxQBQ-iCO9fZS21234nqbqL_mRTsEGQYOnfuHB9_I6OAQstEhAJ_7GwApaE-C8hl0P5uKA9GhSFhDgeTNVC837G9LLT26SzyJWbrg"
            }
        }
    ]

    constructor(private router:Router,
        private auth: AuthService,
        private rest: RestService){}

    ngOnInit() {
        this.trips = [];
        this.rest.getUsersTrip(this.auth.getLoggedUser().id)
        .then(t => {
            console.log("FEACH")
            console.log(t)
            for(let tr of t){
                this.rest.getPlaceById(tr.places[0])
                .then( d => {
                    const td = {
                        tripId:tr.pk,
                        tripName: tr.tripName,
                        tripDescription: tr.tripDescription,
                        place: {
                            name: d.name,
                            photoref: d.photoRef
                        }
                    }
                    console.log("TRIPDETAILS")
                    console.log(d);
                    this.trips.push(td);
                })
                .catch( e => {
                    console.log(e);
                    return e;
                })
                
            }
        })
        .catch(e => {
            console.log(e)
            this.trips = [];
        })
    }

    redirect(id:string): void {
        this.router.navigate([`tourist/tripDetails/${id}`]);
    }
}