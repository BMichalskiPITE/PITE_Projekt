import { Component, OnInit, OnDestroy } from '@angular/core';
import { Place } from '../../../place';
import { ActivatedRoute } from '@angular/router';
import { RestService } from '../../../shared/rest.service';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { Router } from '@angular/router';

@Component({
  selector: 'trip-details',
  templateUrl: './tripDetails.component.html',
  styleUrls: ['./tripDetails.component.scss']
})
export class TripDetailsComponent implements OnInit, OnDestroy {

  closeResult: string;
  details = {
    tripId: 12,
    tripName: "nazwa tripa",
    tripDescription: "opis ktory ktos dal",
    places:[
        {
            placeId: "id",
            latitude: 52,
            longitude: 21,
            name: "nazwa",
            photoRef: "CmRaAAAAEnf6pOTUJdMv0aC-5ukwXNY74FKVl-kPCEmnhX-eSodHY3ZKukK5170GUfwlrHnGj3IDhNoeqWeFe0hlDVxQBQ-iCO9fZS21234nqbqL_mRTsEGQYOnfuHB9_I6OAQstEhAJ_7GwApaE-C8hl0P5uKA9GhSFhDgeTNVC837G9LLT26SzyJWbrg"              ,
            vicinty: "dfghjo"
        }
      ],
    guides:[
        //lista opcjonalnych przewodnikow ktorzy chca wziac wycieczke :D
        {
          id:"id googlowe",
          username:"nazwa user",
          grade: 4.12,// jesl iwogole kiedys to zrobiimy XD
          selected: false
      },
      {
        id:"id googlowe2",
        username:"nazwa user2",
        grade: 4.22,// jesl iwogole kiedys to zrobiimy XD
        selected: false
      }
    ]
  }
  private sub;
  id:Number;

  constructor(private activate:ActivatedRoute,
    private modalService: NgbModal,
    private rest:RestService,
    private router:Router
  ){}

  navigate(id) {
    this.router.navigate(['/profile',id]);
  }

  open(content) {
    
      this.modalService.open(content).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return  `with: ${reason}`;
    }
  }

    selectGuide(guide):void{
      let updateGuide = this.details.guides.find(this.findIndexToUpdate, guide.id)
      let index = this.details.guides.indexOf(updateGuide);
       this.details.guides[index].selected = true;
    }

    findIndexToUpdate(newItem) { 
        return newItem.id === this;
    }

    ngOnInit() {
      this.sub = this.activate.params.subscribe(params => {
         this.id = +params['id'];
         this.details = undefined;
         this.rest.getTripDetails(this.id)
         .then(t => {
            this.details = {
              tripId:t.pk,
              tripName: t.tripName,
              tripDescription: t.tripDescription,
              places: [],
              guides: []
          }
             for(let tr of t.places){
                 this.rest.getPlaceById(tr)
                 .then(pl => this.details.places.push(pl))
                 .catch( e => {
                     return e;
                 })
             }
            for(let tr of t.guides){
              this.rest.getUser(tr)
              .then(pl => this.details.guides.push(pl))
              .catch( e => {
                  return e;
              })
          }
         })
         .catch(e => {
             this.details = undefined;
         })
      });

    }
  
    ngOnDestroy() {
      this.sub.unsubscribe();
    }

  
}
