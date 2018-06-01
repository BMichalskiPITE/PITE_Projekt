import { Component, OnInit } from '@angular/core';
import { MessageService } from '../../shared/message.service';
import { Message } from '../../message';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'message',
  templateUrl: './message.component.html',
  styleUrls: ['./message.component.scss']
})
export class MessageComponent implements OnInit {

  messages: Message[];

  constructor(private messageService: MessageService) { }

  ngOnInit() {
    this.refresh();
  }

  refresh() {
    this.messageService.getMessages().subscribe(msgs => this.messages = msgs);
  }

}
