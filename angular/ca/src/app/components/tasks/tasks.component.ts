import { Component, OnInit } from '@angular/core';
import { PR } from '../../models/PR';
import { CaDataService } from '../../services/ca-data.service';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {

  constructor(public caservice: CaDataService) { }
	public PRData: JSON;
  public newPR = new PR(null , null , null , null , null , null);
  public button = "Add";
  public newRelation = null;
  public relations = ['Cultural Events', 'Cultural Festival', 'Dance Society', 
  									'Literary Society', 'Music Society', 'Theatre Society', 'Fine Arts Society',
  									'Quiz Society', 'Others']

  ngOnInit(): void {
  	this.caservice.getPRs()
  	.then((data) => {
  		console.log(data.json());
  		this.PRData = data.json();
  	})
  }
    get diagnostic() { return JSON.stringify(this.newPR); }

   addPR(){
   	this.button = "Adding..";
   	console.log("creating new PR")
   	if(this.newPR.related_to=="Others"){
   		this.newPR.related_to = this.newRelation;
   	}
   this.caservice.createNewPR(this.newPR)
  	.then((data) => {
  		console.log(data.json());
  		this.button = "Added";
  		this.caservice.getPRs()
  		.then((data) => {
  		console.log(data.json());
  		this.PRData = data.json();
  	})
  	})	
   } 

   othersChoosen(){
   	if(this.newPR.related_to=="Others"){
   		return true;
   	}else{
   		return false;
   	}
   }
}
