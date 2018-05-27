import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../shared/auth.service';
import { RestService } from '../../shared/rest.service';

@Component({
  selector: 'user-profile',
  templateUrl: './userProfile.component.html',
})
export class UserProfileComponent implements OnInit{

  userIdGuide:boolean = false;
  username:string;
  constructor(
    private authService: AuthService,
    private rest:RestService
  ) {}
  
  public ngOnInit():void {
    this.authService.subscribeLoggedUser().subscribe(u => {
      this.userIdGuide = u.is_guide;
      this.username = u.username;
    })
  }
  
  submitUserSettings(){
    const u = this.authService.getLoggedUser();
    u.is_guide = this.userIdGuide;
    this.rest.updateUser(u);
  }
  
}
