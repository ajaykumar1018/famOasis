
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class sceneChange : MonoBehaviour
{
    public void navigateScenes(int scene)
    {
        SceneManager.LoadScene(scene);
    }
    public void covidURL()
    {
        Application.OpenURL("https://www.covid19india.org/");
    }
    public void gameURL()
    {
        Application.OpenURL("https://www.google.com/");
    }
}
