import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Message } from '../message';

@Injectable()
export class MessageService {
  constructor(private http: HttpClient) { }

  messagesUrl = environment.baseApiUrl + 'api/messages/';

  getMessages() {
    return this.http.get<Message[]>(this.messagesUrl);
  }

  postMessage(msg: Message){
      this.http.post(this.messagesUrl,msg);
  }
}
