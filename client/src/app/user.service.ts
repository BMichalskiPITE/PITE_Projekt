import { Injectable, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../environments/environment';
import { User } from './user';
import { GlobalState } from './shared/global.state';
import { LoggedUser } from './commons/loggedUser'; 
const httpOptions = {
  headers: new HttpHeaders({
  'Content-Type': 'application/json'
  })
};
@Injectable()
export class UserService {
  usersUrl = environment.baseApiUrl + 'api/users/';
  logged:LoggedUser;
  constructor(private http: HttpClient, private global: GlobalState) {
    this.global.subscribe("loggedUser", user =>{
      this.logged = user;
    });
  }
  getUser(id: number) {
    return this.http.get<User>(this.usersUrl + id + '/');
  }
  putUser(user: User) {
    return this.http.put<User>(this.usersUrl + user.user_id + '/',user,httpOptions);
  }
}
