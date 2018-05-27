import { Component, OnInit } from '@angular/core';
import { Place } from '../../../place';
import { Router } from '@angular/router';
import { RestService } from '../../../shared/rest.service';


@Component({
  selector: 'gind-trips',
  templateUrl: './findTrips.component.html',
  styleUrls: ['./findTrips.component.scss']
})
export class FindTripsComponent implements OnInit {

    trips = [
        // {
        //     tripId: "21",
        //     tripName: "nazwa mojej superowej  wycieczkie",
        //     tripDescription: "Opis jakiegos miejsca, ktory ktos sobie oddał",
        //     place: {
        //         name: "nazwa miejsca 1",
        //         photoref: "CmRaAAAAEnf6pOTUJdMv0aC-5ukwXNY74FKVl-kPCEmnhX-eSodHY3ZKukK5170GUfwlrHnGj3IDhNoeqWeFe0hlDVxQBQ-iCO9fZS21234nqbqL_mRTsEGQYOnfuHB9_I6OAQstEhAJ_7GwApaE-C8hl0P5uKA9GhSFhDgeTNVC837G9LLT26SzyJWbrg"
        //     },
        //     author: {
        //         id: "id",
        //         name: "jakis autor"
        //     },
        //     isDeclared: true
        // },
        // {
        //     tripId: "12",
        //     tripName: "nazwa1",
        //     tripDescription: "opis1",
        //     place: {
        //         name: "nazwa miejsca 1",
        //         photoref: "CmRaAAAAEnf6pOTUJdMv0aC-5ukwXNY74FKVl-kPCEmnhX-eSodHY3ZKukK5170GUfwlrHnGj3IDhNoeqWeFe0hlDVxQBQ-iCO9fZS21234nqbqL_mRTsEGQYOnfuHB9_I6OAQstEhAJ_7GwApaE-C8hl0P5uKA9GhSFhDgeTNVC837G9LLT26SzyJWbrg"
        //     },
        //     author: {
        //         id: "id",
        //         name: "jakis autor"
        //     },
        //     isDeclared: false
        // }
    ]

    constructor(private router:Router, private rest:RestService){}

    ngOnInit() {
        this.trips = [];
        this.rest.getAllTrips()
        .then(t => {
            console.log("FEACH")
            console.log(t)
            for(let tr of t){
                this.rest.getPlaceById(tr.places[0])
                .then( d => {
                    this.rest.getUser(tr.userId)
                    .then(u => {
                        const td = {
                            tripId:tr.pk,
                            tripName: tr.tripName,
                            tripDescription: tr.tripDescription,
                            place: {
                                name: d.name,
                                photoref: d.photoRef
                            },
                            author:{
                                id: u.id,
                                name: u.username
                            },
                            isDeclared: false
                        }
                        console.log("TRIPDETAILS")
                        console.log(d);
                        this.trips.push(td);
                    })
                    .catch( e => {
                        console.log(e);
                        return e;
                    })
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

    declare(id:String):void {

    }

    removeDeclaration(id:String):void {

    }

    author(id:String):void {

    }
}