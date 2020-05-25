//A simple implementation a clock with multiple threads.
//Clock display format - HH:MM:SS

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>	//Header file for sleep().
#include<pthread.h>
#include<semaphore.h>
#include<time.h>

int hour, min, sec ;
sem_t mutex;
void *hours(){
	while(1){
		sem_wait(&mutex);
		if(min == 60){
			if(hour == 23){
				hour = 0;
			}
			else{
				hour = hour + 1;
			}
			min = 0;
			sec = 0;
		}
		sem_post(&mutex);
	}
}

void *minutes(){
	while(1){
		sem_wait(&mutex);
		if(sec == 60){
			min = min + 1;
			sec = 0;
		}
		sem_post(&mutex);
	}
}

void *seconds(){
	while(1){
		sem_wait(&mutex);
		sec = sec + 1;
		sem_post(&mutex);
	}
}

void *time_display(){
	pthread_t thread_id1, thread_id2, thread_id3;
	
	pthread_create(&thread_id1, NULL, seconds, NULL);
	pthread_create(&thread_id2, NULL, minutes, NULL);
	pthread_create(&thread_id3, NULL, hours, NULL);
	
	while(1){
		printf("\r%02d : %02d : %02d", hour, min , sec);
	}
	pthread_join(thread_id1, NULL);
	pthread_join(thread_id2, NULL);
	pthread_join(thread_id3, NULL);
}

int main(){
	time_t s, val = 1;
	struct tm* current_time;
	s = time(NULL);
	current_time = localtime(&s);
	
	int hr = current_time -> tm_hour;
	int minute = current_time -> tm_min;
	int second = current_time -> tm_sec;
	
	//Initializing Semaphore
	sem_init(&mutex, 0, 1); 
	
	pthread_t thread_id4;
	
	hour = hr;
	min = minute;
	sec = second;
	
	pthread_create(&thread_id4, NULL, time_display, NULL);
	
	pthread_join(thread_id4, NULL);
	
	//Destroying Semaphore
	sem_destroy(&mutex);
	return 0;

}

