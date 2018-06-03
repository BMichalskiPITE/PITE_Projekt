import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../shared/auth.service';
import { RestService } from '../../shared/rest.service';
import { ActivatedRoute } from '@angular/router';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'user-profile',
  templateUrl: './userProfile.component.html',
})
export class UserProfileComponent implements OnInit{

  private sub;
  private user; 
  constructor(
    private authService: AuthService,
    private rest:RestService,
    private activate:ActivatedRoute
  ) {}
  
  images = [
    'http://vacationxtravel.com/wp-content/uploads/2014/02/Most-Visited-Tourist-Attractions-of-The-World1.jpg',
    'http://4.bp.blogspot.com/-cXPqQWpnt9g/UD8NEUVeICI/AAAAAAAAIy8/y1H3Ty1J4N4/s1600/Eiffel+Tower.jpg',
    'http://story.tourders.com/wp-content/uploads/2015/12/chiang-mai-2-1024x768.jpg',
    'http://lovekrakow.pl/images/artykuly_zdjecia/981509455693.jpg',
    'http://polygamia.pl/wp-content/im/7/10168/z10168567O,Smok-Wawelski-kolo-jamy.jpg'
  ]
  index = 0;
  public ngOnInit():void {
    this.sub = this.activate.params.subscribe(params => {
      const id = params['id'];
      this.index = +id % this.images.length;
      this.rest.getUserById(id).then(r => {
        this.user = r;
      })
    });
  }
  
  guide(v){
    this.user.is_guide = v;
    this.rest.updateUser(this.user).then(e => this.authService.setLoggedUser(this.user))
  }


starList: boolean[] = [true,true,true,true,true]; 
rating:number;
setStar(data:any){
      this.rating=data+1;                               
      for(let i=0;i<=4;i++){  
        if(i<=data){  
          this.starList[i]=false;  
        }  
        else{  
          this.starList[i]=true;  
        }  
     }
     this.user.gradesSum += this.rating;
     this.user.gradesNumber += 1; 

     this.rest.updateUser(this.user); 
 }

  getGrade():string {
    if(!this.user) return "0";
    if(!this.user.gradesNumber) {
      return "0";
    } else return (this.user.gradesSum / this.user.gradesNumber).toFixed(1);
  }

  isLogged():boolean {
    
    return this.user && this.authService.getLoggedUser().id == this.user.id;
  }



}