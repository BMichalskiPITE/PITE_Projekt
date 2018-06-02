import { Component, OnInit } from '@angular/core';
import { MessageService } from '../../shared/message.service';
import { Message } from '../../message';
import { Observable } from 'rxjs/Observable';
import { AuthService } from '../../shared/auth.service';
import { RestService } from '../../shared/rest.service';
import { User } from '../../user';

@Component({
  selector: 'message',
  templateUrl: './message.component.html',
  styleUrls: ['./message.component.scss']
})
export class MessageComponent implements OnInit {

  messages: any[];
  toUserId: string;
  message: string;
  users: any[];

  constructor(private auth: AuthService,
              private rest: RestService) { }

  ngOnInit() {
    
    this.rest.getUsers().then(
      users => this.users = users
    ).then(
      x => { this.refresh(); return x; }
    )
  }

  refresh() {
    if(!this.auth.getLoggedUser()){
      return;
    }
    this.rest.getMessages(this.auth.getLoggedUser().id).then(
      msgs => this.messages = msgs.map(m => { 
        let mappedMsg: any = m;
        mappedMsg.fromUsername = this.users.find(u => u.id === m.fromUserId).username
        mappedMsg.toUsername = this.users.find(u => u.id === m.toUserId).username
        return mappedMsg; 
      })
    );
  }

  onSubmit(){
    this.rest.postMessage(this.auth.getLoggedUser().id,this.toUserId,this.message).then( () => this.refresh());
  }

}
