import { TestBed, inject } from '@angular/core/testing';
import { CaDataService } from './ca-data.service';

describe('CaDataService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CaDataService]
    });
  });

  it('should be created', inject([CaDataService], (service: CaDataService) => {
    expect(service).toBeTruthy();
  }));
});
