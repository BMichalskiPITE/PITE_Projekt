import { Component, OnInit } from '@angular/core';
import { Place } from '../../../place';
import { Router } from '@angular/router';
import { RestService } from '../../../shared/rest.service';
import { AuthService } from '../../../shared/auth.service';


@Component({
  selector: 'guide-trips',
  templateUrl: './guideTrips.component.html',
  styleUrls: ['./guideTrips.component.scss']
})
export class GuideTripsComponent implements OnInit {

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
        //     isSelected: true
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
        //     }
        // }
    ]

    constructor(private router:Router,
        private rest:RestService,
        private auth:AuthService
    ){}

    ngOnInit() {
        this.trips = [];
        this.rest.getAllTrips()
        .then(t => {
            for(let tr of t){
                if(!tr.guides || tr.guides[0] !== this.auth.getLoggedUser().id) continue;
                
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
                            }
                        }
                        this.trips.push(td);
                    })
                    .catch( e => {
                        return e;
                    })
                })
                .catch( e => {
                    return e;
                })
                
            }
        })
        .catch(e => {
            this.trips = [];
        })
    }

    redirect(id:string): void {
        this.router.navigate([`tourist/tripDetails/${id}`]);
    }

    removeDeclaration(id:String):void {
        this.rest.removeDeclarationGuide(id, this.auth.getLoggedUser().id).then(e => this.ngOnInit())
    }

    author(id:String):void {
        this.router.navigate(["/profile",id]);
    }
}