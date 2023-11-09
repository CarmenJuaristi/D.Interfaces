package com.example.mycatalog;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class AboutActivityViewModel extends ViewModel {

    private final MutableLiveData<String> mText;

    //Instanciamos el texto que se ve en AboutActivity
    public AboutActivityViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("No me entraba toda la letra de la canción, pero se llama Versos Perversos y es una obra de arte");
    }

    public LiveData<String> getText() {
        return mText;
    }
}